from spirit.game.card_effects.pokemon import primate_wisdom
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0f9e0a4c-12de-5997-be84-1ba3070fb6ee",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=199,
    set_code="SWSH4",
    rarity=Rarities.RareSecret,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Ability(
            title="Primate Wisdom",
            game_text="Once during your turn, you may switch a card from your hand with the top card of your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=primate_wisdom,
        ),
        Attack(
            title="Whap Down",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)