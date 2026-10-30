"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    delta_edge_supporter_bonus,
    fossil_charge_snipe,
)

card = PokemonCardDef(guid='f4f53d54-4fe2-570f-aceb-1ec89ffb1743', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name', display_name='Armaldo δ', searchable_by=['Armaldo δ', 'Stage 2', 'Armaldo'], subtypes=['Stage 2'], collector_number=1, set_code='EX13', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name', family_id=348, abilities=[Attack(title='Delta Edge', game_text="If you have any Supporter cards in play, this attack's base damage is 20 instead of 70.", cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1}, damage=70, effect=delta_edge_supporter_bonus(70, 20)), Attack(title='Fossil Charge', game_text="You may discard a Claw Fossil, Mysterious Fossil, Root Fossil, or Holon Fossil from your hand. If you do, choose 1 of your opponent's Benched Pokémon and do 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50, effect=fossil_charge_snipe(30))])
