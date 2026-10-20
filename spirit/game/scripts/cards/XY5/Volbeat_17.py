from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_damage, bonus_if


card = PokemonCardDef(
    guid="c0bb20c9-daf2-564a-b549-813788b015ce",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
        Attack(
            title="Pester",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and bool(ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS)), 30),
        ),
    ],
)