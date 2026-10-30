from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import constrain_discard_to, upstream_discard_energy_damage

card = PokemonCardDef(
    guid="795bbe86-dc81-51cb-96d2-a76c44e98582",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcattyex.Name",
    display_name="Delcatty ex",
    searchable_by=["Delcatty ex", "Stage 1", "ex", "Delcattyex"],
    subtypes=["Stage 1", "ex"],
    collector_number=91,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Constrain",
            game_text="Once during your turn (before your attack), you may use this power. Each player discards cards until that player has 6 cards in his or her hand. (You discard first.) This power can't be used if Delcatty ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
                        effect=constrain_discard_to(6),
        ),
        Attack(
            title="Upstream",
            game_text="Search your discard pile for all Energy cards. This attack does 10 damage times the number of Energy cards you find there. Show them to your opponent, and put them on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
                        effect=upstream_discard_energy_damage(10),
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)