"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    flames_of_rage,
    wreck_stadium,
)

card = PokemonCardDef(guid='36eed11d-33d0-5b52-afd4-4719e35a63a1', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name', display_name='Primeape δ', searchable_by=['Primeape δ', 'Stage 1', 'Primeape'], subtypes=['Stage 1'], collector_number=50, set_code='EX13', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name', family_id=57, abilities=[Attack(title='Wreck', game_text='If there is any Stadium card in play, this attack does 30 damage plus 30 more damage. Discard that Stadium card.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1}, damage=30, damage_operator='+', effect=wreck_stadium(30, 30)), Attack(title='Flames of Rage', game_text='Discard 2 Energy attached to Primeape. This attack does 10 damage plus 20 more damage for each damage counter on Primeape.', cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+', effect=flames_of_rage(10, 20))])
