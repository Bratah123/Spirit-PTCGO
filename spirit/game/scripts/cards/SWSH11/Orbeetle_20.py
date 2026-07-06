from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a1069e17-851c-5fd0-a33f-c5248c8df9f1",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Jamming Attachment",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach up to 3 Energy cards from your opponent's discard pile to your opponent's Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)