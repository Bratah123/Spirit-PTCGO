from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="49dab7f1-a23f-5747-954d-9305cf47d5df",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Vitality Spring",
            game_text="Once during your turn, you may search your deck for up to 6 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)