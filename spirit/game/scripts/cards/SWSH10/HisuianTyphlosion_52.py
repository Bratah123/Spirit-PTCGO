from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="322b0073-6630-5cfb-9494-ed708adfb6d9",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosion.Name",
    display_name="Hisuian Typhlosion",
    searchable_by=["Hisuian Typhlosion", "Stage 2", "HisuianTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Supernatural Orb",
            game_text="You must discard a Psychic Energy card from your hand in order to use this Ability. Once during your turn, you may make your opponent's Active Pok\u00e9mon Burned and Confused.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=unimplemented,
        ),
    ],
)