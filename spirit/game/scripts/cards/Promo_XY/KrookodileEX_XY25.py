"""STUB: effect not implemented — do not guess mechanics.
Krookodile-EX (Promo_XY #XY25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="04ee1c3c-f304-53ab-891e-c55b8646dfcf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KrookodileEX.Name",
    display_name="Krookodile-EX",
    searchable_by=["Krookodile-EX", "Basic", "EX", "KrookodileEX"],
    subtypes=["Basic", "EX"],
    collector_number=25,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=553,
    abilities=[
        Attack(
            title="Second Bite",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Megaton Fang",
            game_text="Discard a card from your hand. If you can't discard a card, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)