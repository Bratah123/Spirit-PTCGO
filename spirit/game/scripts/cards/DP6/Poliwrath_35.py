"""DP6 Legends Awakened — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp6_poliwrath_35_focus_punch,
    dp6_poliwrath_35_submission,
)

card = PokemonCardDef(guid='f484bd6b-96de-5b90-93b9-c3fd428327d2', key='DP6', name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name', display_name='Poliwrath', searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'], subtypes=['Stage 2'], collector_number=35, set_code='DP6', rarity=Rarities.Rare, hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name', family_id=60, abilities=[Attack(title='Focus Punch', game_text="If Poliwrath was damaged by an attack during your opponent's last turn, this attack does nothing.", cost={PokemonTypes.FIGHTING: 1}, damage=60, effect=dp6_poliwrath_35_focus_punch()), Attack(title='Submission', game_text='Poliwrath does 20 damage to itself.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=90, effect=dp6_poliwrath_35_submission())])
