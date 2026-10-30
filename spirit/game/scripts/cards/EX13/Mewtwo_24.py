"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import amnesia
from spirit.game.card_effects.ex import (
    swift_attack,
)

card = PokemonCardDef(guid='b1c32416-f4d2-502b-8bfc-de5c6b969def', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name', display_name='Mewtwo δ', searchable_by=['Mewtwo δ', 'Basic', 'Mewtwo'], subtypes=['Basic'], collector_number=24, set_code='EX13', rarity=Rarities.Rare, hp=70, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=150, abilities=[Attack(title='Psychic Erase', game_text="Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, effect=amnesia), Attack(title='Swift', game_text="This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.", cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=40, effect=swift_attack())])
