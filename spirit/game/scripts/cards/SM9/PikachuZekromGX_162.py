from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    full_blitz,
    tag_bolt_gx,
)

card = PokemonCardDef(
    guid="9eb370c5-457c-524b-862f-a78d63f3cca1",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuZekromGX.Name",
    display_name="Pikachu & Zekrom-GX",
    searchable_by=["Pikachu & Zekrom-GX", "Basic", "TAG TEAM", "GX", "PikachuZekromGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=162,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Full Blitz",
            game_text="Search your deck for up to 3 Lightning Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=full_blitz,
        ),
        Attack(
            title="Tag Bolt-GX",
            game_text="If this Pok\u00e9mon has at least 3 extra Lightning Energy attached to it (in addition to this attack's cost), this attack does 170 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            effect=tag_bolt_gx,
        ),
    ],
)