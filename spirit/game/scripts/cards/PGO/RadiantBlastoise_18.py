from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76360f77-185a-5c93-9e8e-b9cc93cc38e9",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantBlastoise.Name",
    display_name="Radiant Blastoise",
    searchable_by=["Radiant Blastoise", "Basic", "Radiant", "RadiantBlastoise"],
    subtypes=["Basic", "Radiant"],
    collector_number=18,
    set_code="PGO",
    rarity=Rarities.RareRadiant,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=9,
    abilities=[
        Ability(
            title="Pump Shot",
            game_text="You must discard a Water Energy card from your hand in order to use this Ability. Once during your turn, you may put 2 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Torrential Cannon",
            game_text="During your next turn, this Pok\u00e9mon can't use Torrential Cannon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)