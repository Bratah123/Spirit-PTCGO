from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import call_for_family_basic_n, crush_chance_on_play


card = PokemonCardDef(
    guid="5b5494ef-3ca4-53a0-a479-765193e1e595",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Ability(
            title="Crush Chance",
            game_text="Once during your turn, when you put Tauros from your hand onto your Bench, you may discard a Stadium card in play.",
            ability_type=AbilityTypes.POKE_POWER,
                        effect=crush_chance_on_play(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family_basic_n(2),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)