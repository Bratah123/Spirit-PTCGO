"""DP3 Secret Wonders — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    dp3_salamence_18_direct_hit,
    dp3_salamence_18_dragon_finish,
)

card = PokemonCardDef(guid='7b5539cb-3d94-5c77-9c04-9ca942e2740f', key='DP3', name='com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name', display_name='Salamence', searchable_by=['Salamence', 'Stage 2', 'Salamence'], subtypes=['Stage 2'], collector_number=18, set_code='DP3', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.COLORLESS, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name', family_id=371, abilities=[Attack(title='Direct Hit', game_text="This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.", cost={PokemonTypes.COLORLESS: 2}, damage=50, effect=dp3_salamence_18_direct_hit()), Attack(title='Dragon Finish', game_text="Discard 2 basic Fire Energy cards or 2 basic Water Energy cards attached to Salamence. If you discarded 2 basic Fire Energy cards, this attack does 100 damage to the Defending Pokémon. If you discarded 2 Basic Water Energy cards, this attack does 100 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (If you can't discard cards, this attack does nothing.)", cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 2}, effect=dp3_salamence_18_dragon_finish())])
