"""STUB: effect not implemented — do not guess mechanics.
Groudon ★ (EX11 #111): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import critical_collection, discard_typed_energy_after
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c732efa-6de7-5a74-890c-d164244d2bfa",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon ★",
    searchable_by=["Groudon \u2605", "Basic", "Star", "Groudon"],
    subtypes=["Basic", "Star"],
    collector_number=111,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Attack(
            title="Critical Collection",
            game_text="Count the number of Prize cards your opponent has taken. Search your discard pile for up to that many Fighting Energy cards and attach them to Groudon Star.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=critical_collection(PokemonTypes.FIGHTING),
        ),
        Attack(
            title="Ground Slash",
            game_text="Discard a Fighting Energy card attached to Groudon Star.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=discard_typed_energy_after(PokemonTypes.FIGHTING, 80),
        ),
    ],
)