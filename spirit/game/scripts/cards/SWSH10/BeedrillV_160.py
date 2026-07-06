from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9cab229-fbc2-50be-ba16-37a9eb097305",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillV.Name",
    display_name="Beedrill V",
    searchable_by=["Beedrill V", "Basic", "V", "BeedrillV"],
    subtypes=["Basic", "V"],
    collector_number=160,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=15,
    abilities=[
        Attack(
            title="Twineedle",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Swarming Sting",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon for each of your Beedrill V in play. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)