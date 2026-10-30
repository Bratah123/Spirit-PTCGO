"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import (
    charity_tail,
    tail_influence,
)

card = PokemonCardDef(guid='361855fb-76ab-5b94-b0d4-b2fbbc36f3f6', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name', display_name='Ambipom', searchable_by=['Ambipom', 'Stage 1', 'Ambipom'], subtypes=['Stage 1'], collector_number=3, set_code='DP2', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name', family_id=190, abilities=[Attack(title='Tail Influence', game_text="Your opponent flips a coin until he or she gets heads. For each tails, remove an Energy card attached to the Defending Pokémon and put it on the bottom of your opponent's deck.", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=tail_influence()), Attack(title='Charity Tail', game_text="Before Ambipom does damage, your opponent may discard 2 cards from his or her hand. If he or she does, this attack's base damage is 10 instead of 80.", cost={PokemonTypes.COLORLESS: 2}, damage=80, effect=charity_tail(80, 2))])
