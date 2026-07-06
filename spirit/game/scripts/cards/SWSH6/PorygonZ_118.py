from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b4fde7b-7d08-5b05-ba8e-8ba7a5b8fd80",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=118,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Bug Transmission",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon during your turn, you may make your opponent's Active Pok\u00e9mon Confused.",
            effect=unimplemented,
        ),
        Attack(
            title="Superbeam",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=unimplemented,
        ),
    ],
)