from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="19405b49-dd40-5516-beb3-1920a1dbdb9e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name="Hatterene",
    searchable_by=["Hatterene", "Stage 2", "Hatterene"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Ability(
            title="Witch Rondo",
            game_text="Once during your turn, you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)