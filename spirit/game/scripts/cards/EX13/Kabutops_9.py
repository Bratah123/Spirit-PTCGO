"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    thunderous_blow,
    vital_drain_on_ko,
)

card = PokemonCardDef(guid='8ad5530e-a646-5732-87bb-ec20398b18ab', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name', display_name='Kabutops δ', searchable_by=['Kabutops δ', 'Stage 2', 'Kabutops'], subtypes=['Stage 2'], collector_number=9, set_code='EX13', rarity=Rarities.RareHolo, hp=100, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name', family_id=141, abilities=[Attack(title='Vital Drain', game_text='If the Defending Pokémon is Knocked Out by this attack, remove all Special Conditions and 7 damage counters from Kabutops (all if there are less than 7).', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=vital_drain_on_ko(7)), Attack(title='Thunderous Blow', game_text='Does 40 damage plus 10 more damage for each Lightning Energy attached to Kabutops.', cost={PokemonTypes.COLORLESS: 3}, damage=40, damage_operator='+', effect=thunderous_blow(40, 10))])
