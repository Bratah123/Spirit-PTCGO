from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a40159a4-cfe1-5475-8c4d-ead32f6ed1f0",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Shining Arcana",
            game_text="Once during your turn, you may look at the top 2 cards of your deck and attach any number of basic Energy cards you find there to your Pok\u00e9mon in any way you like. Put the other cards into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Brainwave",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)