"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    assurance_damaged_last_turn,
)
from spirit.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(guid='f518eccf-1867-51e0-8830-09fa63a219f1', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Rampardos.Name', display_name='Rampardos', searchable_by=['Rampardos', 'Stage 2', 'Rampardos'], subtypes=['Stage 2'], collector_number=33, set_code='DP2', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name', family_id=408, abilities=[Attack(title='Assurance', game_text="As long as the Defending Pokémon's remaining HP is 60 or less, this attack's base damage is 60 instead of 30.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=assurance_damaged_last_turn(30, 40)), Attack(title='Hasty Headbutt', game_text="Rampardos does 20 damage to itself. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.", cost={PokemonTypes.FIGHTING: 3}, damage=100, effect=flip_or_nothing())])
