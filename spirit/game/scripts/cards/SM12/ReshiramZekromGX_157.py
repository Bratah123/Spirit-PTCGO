from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import fabled_flarebolts, cross_break_gx

card = PokemonCardDef(
    guid="d8b99594-9db9-5eb9-b0c1-7507837e6a86",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramZekromGX.Name",
    display_name="Reshiram & Zekrom-GX",
    searchable_by=["Reshiram & Zekrom-GX", "Basic", "TAG TEAM", "GX", "ReshiramZekromGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=157,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=643,
    abilities=[
        Attack(
            title="Fabled Flarebolts",
            game_text="Discard up to 3 in any combination of basic Fire and basic Lightning Energy cards from your Benched Pok\u00e9mon. This attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=90,
            damage_operator="x",
            effect=fabled_flarebolts,
        ),
        Attack(
            title="Cross Break-GX",
            game_text="This attack does 170 damage to 1 of your opponent's Benched Pok\u00e9mon. If you played N's Resolve from your hand during this turn, this attack also does 170 damage to 1 of your opponent's other Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            effect=cross_break_gx,
        ),
    ],
)