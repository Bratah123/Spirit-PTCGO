from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff63c087-6d3f-56ef-84ef-7edc9bd0429b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Puppet Offering",
            game_text="Once during your turn, you may put a Supporter card from your discard pile into your hand. If you do, put this Pok\u00e9mon in the Lost Zone. (Discard all attached cards.)",
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)