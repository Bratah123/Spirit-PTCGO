"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import (
    energy_absorption_self,
    psychic_star,
)

card = PokemonCardDef(guid='ea90972e-24a4-52b6-bac6-99b55b13c2d2', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name', display_name='Mewtwo ★', searchable_by=['Mewtwo ★', 'Basic', 'Star', 'Mewtwo'], subtypes=['Basic', 'Star'], collector_number=103, set_code='EX13', rarity=Rarities.RareHolo, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=150, abilities=[Attack(title='Energy Absorption', game_text='Search your discard pile for an Energy card and attached it to Mewtwo Star.', cost={PokemonTypes.COLORLESS: 1}, effect=energy_absorption_self()), Attack(title='Psychic Star', game_text='If the Defending Pokémon is an Evolved Pokémon, discard all Energy attached to Mewtwo Star and this attack does 50 damage plus 50 more damage.', cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1}, damage=50, damage_operator='+', effect=psychic_star())])
