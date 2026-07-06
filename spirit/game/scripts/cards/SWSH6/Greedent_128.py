from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7d190e5c-e7c5-5860-9d7a-7f42fd27702a",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name",
    display_name="Greedent",
    searchable_by=["Greedent", "Stage 1", "Greedent"],
    subtypes=["Stage 1"],
    collector_number=128,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    family_id=819,
    abilities=[
        Ability(
            title="Brazen Tail",
            game_text="Energy attached to your Pok\u00e9mon can't be put into your hand, deck, or discard pile by an effect of your opponent's Item or Supporter cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)