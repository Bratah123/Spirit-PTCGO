from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import baby_evolution, baby_evolution_condition
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card


card = PokemonCardDef(
    guid="fd878247-e2b6-55cb-b3f7-3d908179dfc3",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Marill from your hand onto Azurill (this counts as evolving Azurill), and remove all damage counters from Azurill.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=baby_evolution_condition("Marill"),
            effect=baby_evolution("Marill"),
        ),
        Attack(
            title="Jump Catch",
            game_text="Search your deck for a Trainer card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                is_trainer_card, count=1, reveal=True,
                prompt="Choose a Trainer card.",
            ),
        ),
    ],
)
