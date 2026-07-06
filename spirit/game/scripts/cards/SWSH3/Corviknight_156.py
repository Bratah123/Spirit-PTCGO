from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3878f503-8254-5362-8157-3818792e1f60",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name",
    display_name="Corviknight",
    searchable_by=["Corviknight", "Stage 2", "Corviknight"],
    subtypes=["Stage 2"],
    collector_number=156,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    family_id=821,
    abilities=[
        Ability(
            title="Flying Taxi",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 1 of your Pok\u00e9mon, except any Corviknight, and all attached cards into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)