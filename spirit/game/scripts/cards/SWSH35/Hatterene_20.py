from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6b48707-12f3-59da-9660-ae6568c803c0",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name="Hatterene",
    searchable_by=["Hatterene", "Stage 2", "Hatterene"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Ability(
            title="Hazard Sensor",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Confused.",
            effect=unimplemented,
        ),
        Attack(
            title="Life Sucker",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)