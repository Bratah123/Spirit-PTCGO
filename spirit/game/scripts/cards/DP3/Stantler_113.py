"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.dp import inviting_bell
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(guid='a73d1705-7638-5471-ab36-7a9b2d488b6f', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name', display_name='Stantler', searchable_by=['Stantler', 'Basic', 'Stantler'], subtypes=['Basic'], collector_number=113, set_code='DP3', rarity=Rarities.Common, hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=234, abilities=[Attack(title='Lead', game_text='Search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.', cost={}, effect=inviting_bell()), Attack(title='Frighten Horn', game_text="If the Defending Pokémon isn't an Evolved Pokémon, that Pokémon is now Confused.", cost={PokemonTypes.COLORLESS: 2}, damage=20, effect=condition_attack(SpecialConditions.CONFUSED))])
