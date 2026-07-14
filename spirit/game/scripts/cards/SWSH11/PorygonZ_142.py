from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.pokemon import downgrading_beam
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6d4a6fa-6b86-5d5c-a537-c0bdf3d38406",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=142,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Downgrading Beam",
            game_text="Devolve 1 of your opponent's evolved Pok\u00e9mon by removing any number of Evolution cards from it. Your opponent shuffles those cards into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=downgrading_beam,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)