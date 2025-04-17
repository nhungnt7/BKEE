#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BKEE Dataset Exploration Script
This script demonstrates how to load and explore the BKEE dataset for
Vietnamese Event Extraction.
"""

import json
import os
from collections import Counter
from typing import List, Dict, Any

def load_jsonl(file_path: str) -> List[Dict[str, Any]]:
    """
    Load data from a JSONL file (JSON Lines)
    
    Args:
        file_path: Path to the JSONL file
        
    Returns:
        List of dictionaries, each representing a document
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
        print(f"Successfully loaded {len(data)} documents from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []

def get_dataset_statistics(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate statistics for the dataset
    
    Args:
        data: List of documents
        
    Returns:
        Dictionary with statistics
    """
    if not data:
        return {"documents": 0}
    
    total_tokens = sum(len(doc.get('tokens', [])) for doc in data)
    total_entity_mentions = sum(len(doc.get('entity_mentions', [])) for doc in data)
    total_event_mentions = sum(len(doc.get('event_mentions', [])) for doc in data)
    total_relation_mentions = sum(len(doc.get('relation_mentions', [])) for doc in data)
    
    # Count event types if available
    event_types = []
    for doc in data:
        for event in doc.get('event_mentions', []):
            if 'event_type' in event:
                event_types.append(event['event_type'])
    
    # Count entity types if available
    entity_types = []
    for doc in data:
        for entity in doc.get('entity_mentions', []):
            if 'entity_type' in entity:
                entity_types.append(entity['entity_type'])
    
    return {
        "documents": len(data),
        "tokens": total_tokens,
        "avg_tokens_per_doc": total_tokens / len(data) if data else 0,
        "entity_mentions": total_entity_mentions,
        "event_mentions": total_event_mentions,
        "relation_mentions": total_relation_mentions,
        "event_types": dict(Counter(event_types)),
        "entity_types": dict(Counter(entity_types)),
    }

def find_examples_with_events(data: List[Dict[str, Any]], limit: int = 3) -> List[Dict[str, Any]]:
    """
    Find examples that contain event mentions
    
    Args:
        data: List of documents
        limit: Maximum number of examples to return
        
    Returns:
        List of documents containing event mentions
    """
    examples = []
    for doc in data:
        if doc.get('event_mentions', []):
            examples.append(doc)
            if len(examples) >= limit:
                break
    return examples

def search_by_event_type(data: List[Dict[str, Any]], event_type: str) -> List[Dict[str, Any]]:
    """
    Search for documents containing a specific event type
    
    Args:
        data: List of documents
        event_type: Event type to search for
        
    Returns:
        List of documents containing the specified event type
    """
    results = []
    for doc in data:
        for event in doc.get('event_mentions', []):
            if 'event_type' in event and event['event_type'] == event_type:
                results.append(doc)
                break  # Only add each document once
    return results

def display_document(doc: Dict[str, Any], show_mentions: bool = True) -> None:
    """
    Display information about a document
    
    Args:
        doc: Document dictionary
        show_mentions: Whether to display entity and event mentions
    """
    print(f"\nDocument ID: {doc.get('doc_id', 'Unknown')}")
    print(f"Sentence ID: {doc.get('sent_id', 'Unknown')}")
    print(f"Sentence: {doc.get('sentence', '')}")
    print(f"Number of tokens: {len(doc.get('tokens', []))}")
    
    if show_mentions:
        if doc.get('entity_mentions', []):
            print("\nEntity Mentions:")
            for i, entity in enumerate(doc.get('entity_mentions', []), 1):
                print(f"  {i}. {entity}")
        
        if doc.get('event_mentions', []):
            print("\nEvent Mentions:")
            for i, event in enumerate(doc.get('event_mentions', []), 1):
                print(f"  {i}. {event}")
        
        if doc.get('relation_mentions', []):
            print("\nRelation Mentions:")
            for i, relation in enumerate(doc.get('relation_mentions', []), 1):
                print(f"  {i}. {relation}")

def analyze_event_types(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Analyze and count event types in the dataset
    
    Args:
        data: List of documents
        
    Returns:
        Dictionary with event types and their counts
    """
    event_types = Counter()
    
    for doc in data:
        for event in doc.get('event_mentions', []):
            if 'event_type' in event:
                event_types[event['event_type']] += 1
    
    return event_types

def analyze_entity_types(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Analyze and count entity types in the dataset
    
    Args:
        data: List of documents
        
    Returns:
        Dictionary with entity types and their counts
    """
    entity_types = Counter()
    
    for doc in data:
        for entity in doc.get('entity_mentions', []):
            if 'entity_type' in entity:
                entity_types[entity['entity_type']] += 1
    
    return entity_types

def analyze_argument_roles(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Analyze and count argument roles in the dataset
    
    Args:
        data: List of documents
        
    Returns:
        Dictionary with argument roles and their counts
    """
    argument_roles = Counter()
    
    for doc in data:
        for event in doc.get('event_mentions', []):
            for arg in event.get('arguments', []):
                if 'role' in arg:
                    argument_roles[arg['role']] += 1
    
    return argument_roles

def search_by_entity_type(data: List[Dict[str, Any]], entity_type: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Search for documents containing entities of a specific type
    
    Args:
        data: List of documents
        entity_type: Entity type to search for
        limit: Maximum number of documents to return
        
    Returns:
        List of matching documents
    """
    results = []
    for doc in data:
        for entity in doc.get('entity_mentions', []):
            if 'entity_type' in entity and entity['entity_type'] == entity_type:
                results.append(doc)
                break  # Only add each document once
        
        if len(results) >= limit:
            break
            
    return results

def main():
    """Main function to demonstrate the usage of BKEE dataset"""
    print("=== BKEE Dataset Exploration ===\n")
    
    # Load the datasets
    train_data = load_jsonl('processed/train.json')
    dev_data = load_jsonl('processed/dev.json')
    test_data = load_jsonl('processed/test.json')
    
    # Display statistics
    print("\n=== Dataset Statistics ===")
    
    print("\nTraining Set:")
    train_stats = get_dataset_statistics(train_data)
    for key, value in train_stats.items():
        if key not in ('event_types', 'entity_types'):
            print(f"  - {key}: {value}")
    
    print("\nDevelopment Set:")
    dev_stats = get_dataset_statistics(dev_data)
    for key, value in dev_stats.items():
        if key not in ('event_types', 'entity_types'):
            print(f"  - {key}: {value}")
    
    print("\nTest Set:")
    test_stats = get_dataset_statistics(test_data)
    for key, value in test_stats.items():
        if key not in ('event_types', 'entity_types'):
            print(f"  - {key}: {value}")
    
    # Display example documents
    print("\n=== Example Documents ===")
    
    # Get examples from the training set that have event mentions
    event_examples = find_examples_with_events(train_data)
    
    if event_examples:
        print(f"\nFound {len(event_examples)} examples with event mentions:")
        for example in event_examples:
            display_document(example)
    else:
        # If no event mentions, just show the first document
        print("\nFirst document in training set:")
        if train_data:
            display_document(train_data[0])
    
    # Analyze event types
    print("\n=== Event Type Analysis ===")
    event_types = analyze_event_types(train_data)
    print(f"Top 10 event types in training data:")
    for event_type, count in event_types.most_common(10):
        print(f"  - {event_type}: {count} instances")
    
    # Analyze entity types
    print("\n=== Entity Type Analysis ===")
    entity_types = analyze_entity_types(train_data)
    print(f"Entity types in training data:")
    for entity_type, count in entity_types.most_common():
        print(f"  - {entity_type}: {count} instances")
    
    # Analyze argument roles
    print("\n=== Argument Role Analysis ===")
    argument_roles = analyze_argument_roles(train_data)
    print(f"Argument roles in training data:")
    for role, count in argument_roles.most_common(10):
        print(f"  - {role}: {count} instances")
    
    # Demonstrate search functionality
    print("\n=== Search Examples ===")
    
    # Find examples with a specific entity type (e.g., GPE - Geo-Political Entity)
    if entity_types:
        common_entity_type = entity_types.most_common(1)[0][0]
        print(f"\nSearching for documents with entity type '{common_entity_type}':")
        entity_examples = search_by_entity_type(train_data, common_entity_type, limit=1)
        if entity_examples:
            display_document(entity_examples[0])
        else:
            print(f"  No examples found for entity type '{common_entity_type}'")
    
    print("\n=== Processing Complete ===")

if __name__ == "__main__":
    main()
