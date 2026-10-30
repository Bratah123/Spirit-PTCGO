"""STUB: effect not implemented — do not guess mechanics.
Metagross ★ (EX11 #113): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import critical_collection
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="f5699a92-fe4d-54c9-a1d4-dd7cf8f7b3e6",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross ★",
    searchable_by=["Metagross \u2605", "Basic", "Star", "Metagross"],
    subtypes=["Basic", "Star"],
    collector_number=113,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=376,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Metal Energy cards and attach them to Metagross Star.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=critical_collection(PokemonTypes.METAL),
        ),
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
    ],
)