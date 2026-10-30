from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.ex import energy_draw, energy_draw_condition


card = PokemonCardDef(
    guid="15795c62-7fcd-54b4-b234-168ee699ed25",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Energy Draw",
            game_text="Once during your turn (before your attack), you may discard 1 Energy card from your hand. Then draw up to 3 cards from your deck. This power can't be used if Delcatty is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=energy_draw_condition,
            effect=energy_draw(),
        ),
        Attack(
            title="Max Energy Source",
            game_text="Does 10 damage times the amount of Energy attached to all of your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("my_active"), 10),
        ),
    ],
)
