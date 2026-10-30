"""STUB: effect not implemented — do not guess mechanics.
Gengar (DP7 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_gengar_18_fainting_spell,
    dp7_gengar_18_poltergeist,
    dp7_gengar_18_shadow_room,
)

card = PokemonCardDef(guid='52be2abc-2aaf-59fa-b4c5-59bbe7357aa2', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name', display_name='Gengar', searchable_by=['Gengar', 'Stage 2', 'Gengar'], subtypes=['Stage 2'], collector_number=18, set_code='DP7', rarity=Rarities.Rare, hp=110, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.COLORLESS, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name', family_id=92, abilities=[Ability(title='Fainting Spell', game_text="Once during your opponent's turn, if Gengar would be Knocked Out by damage from an attack, you may flip a coin. If heads, the Defending Pokémon is Knocked Out.", ability_type=AbilityTypes.POKE_POWER, effect=dp7_gengar_18_fainting_spell(), activation=Activations.ONCE_PER_TURN), Attack(title='Shadow Room', game_text="Put 3 damage counters on 1 of your opponent's Pokémon. If that Pokémon has any Poké-Powers, put 6 damage counters on that Pokémon instead.", cost={PokemonTypes.PSYCHIC: 1}, effect=dp7_gengar_18_shadow_room()), Attack(title='Poltergeist', game_text="Look at your opponent's hand. This attack does 30 damage times the number of Trainer, Supporter, and Stadium cards in your opponent's hand.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='x', effect=dp7_gengar_18_poltergeist())])
