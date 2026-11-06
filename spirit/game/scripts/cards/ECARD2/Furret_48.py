from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import scavenger_hunt, scavenger_hunt_condition


card = PokemonCardDef(
    guid="e6f61d38-b1ff-51f2-9ff6-d46ccd908fb7",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Ability(
            title="Scavenger Hunt",
            game_text="Once during your turn (before your attack), you may put 2 cards from your hand into your deck. Then, search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Furret is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=scavenger_hunt_condition,
            effect=scavenger_hunt,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
