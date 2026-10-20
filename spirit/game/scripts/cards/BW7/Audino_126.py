from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5925c064-7e2c-55cf-baa8-69c7f5df4113",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic", "Audino"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Ability(
            title="Busybody",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your hand, you may reveal it. If you do, heal 10 damage and remove a Special Condition from your Active Pok\u00e9mon. Then, discard this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Hip Bump",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)