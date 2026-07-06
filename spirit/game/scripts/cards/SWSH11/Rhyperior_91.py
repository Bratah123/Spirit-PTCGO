from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2511b893-133b-552f-bd82-df0be95def33",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=91,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Geo Cannon",
            game_text="Discard the top card of your deck. If that card is an Energy card, this attack does 100 more damage, and attach that card to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Rocky Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)