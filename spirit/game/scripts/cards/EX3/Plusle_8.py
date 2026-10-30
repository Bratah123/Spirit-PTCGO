from spirit.game.card_effects.ex import chain_of_events_passive, extra_circuit
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_targets

card = PokemonCardDef(
    guid="a7a9f153-e3a6-5d81-8b43-c5d95dba6f41",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=311,
    abilities=[
        Ability(
            title="Chain of Events",
            game_text="As long as Plusle is your Active Pok\u00e9mon, whenever your other Active Pok\u00e9mon, if any, attacks, you may use Cheer On after the first attack (you still need the necessary Energy to use Cheer On). You can't use Cheer On more than once in this way even if your other Active Pok\u00e9mon has the Chain of Events Pok\u00e9-Body.",
            ability_type=AbilityTypes.POKE_BODY,
            effect=None,
            passive=chain_of_events_passive(),
        ),
        Attack(
            title="Cheer On",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon (including Plusle).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=heal_targets(10, scope="each_own"),
        ),
        Attack(
            title="Extra Circuit",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. If you choose Pok\u00e9mon-ex, this attack does 40 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=extra_circuit(20, 40),
        ),
    ],
)