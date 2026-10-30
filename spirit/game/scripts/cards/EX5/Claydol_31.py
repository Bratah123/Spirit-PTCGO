"""STUB: effect not implemented — do not guess mechanics.
Claydol (EX5 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="5d1eb55a-d97b-56a7-b821-8276f9cedac3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard 1 Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)