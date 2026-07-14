from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, damage_per

card = PokemonCardDef(
    guid="0f3371a0-3777-5d8a-b3e8-9bb8fbf01693",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MiloticV.Name",
    display_name="Milotic V",
    searchable_by=["Milotic V", "Basic", "V", "MiloticV"],
    subtypes=["Basic", "V"],
    collector_number=179,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=350,
    abilities=[
        Attack(
            title="Aqua Impact",
            game_text="This attack does 50 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(
                lambda ctx: (ctx.opponent_active().get_attribute(AttrID.RETREAT_COST, 0)
                             if ctx.opponent_active() else 0),
                50, base=10,
            ),
        ),
        Attack(
            title="Hypno Splash",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)