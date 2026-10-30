from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import delta_draw_up_to

card = PokemonCardDef(
    guid="767fa96a-78de-5cca-9068-4501eb49270b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow δ",
    searchable_by=["Fearow \u03b4", "Stage 1", "Fearow"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX14",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Ability(
            title="Delta Sign",
            game_text="Once during your turn (before your attack), you may search your deck for a Pok\u00e9mon that has \u03b4 on its card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. You can't use more than 1 Delta Sign Pok\u00e9-Power each turn. This power can't be used if Fearow is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
                        effect=delta_draw_up_to(),
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)