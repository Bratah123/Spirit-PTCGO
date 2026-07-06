from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe67fb86-b935-50da-8200-177adde21841",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence",
    searchable_by=["Salamence", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=109,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=371,
    abilities=[
        Ability(
            title="Intimidating Roar",
            game_text="Once during your turn, you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Fierce Dragon",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)