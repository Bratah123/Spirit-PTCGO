from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_targets
from spirit.game.card_effects.ex import special_circuit

card = PokemonCardDef(
    guid="1a7fcd57-5438-5262-86d9-6dad01a1bfdc",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=312,
    abilities=[
        Ability(
            title="Chain of Events",
            game_text="As long as Minun is your Active Pok\u00e9mon, whenever your other Active Pok\u00e9mon, if any, attacks, you may use Cheer On after the first attack (you still need the necessary Energy to use Cheer On). You can't use Cheer On more than once in this way even if your other Active Pok\u00e9mon has the Chain of Events Pok\u00e9-Body.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cheer On",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon (including Minun).",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=heal_targets(10, scope="each_own"),
        ),
        Attack(
            title="Special Circuit",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. If you choose Pok\u00e9mon that has a Pok\u00e9-Power or Pok\u00e9-Body, this attack does 40 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=special_circuit(20, 40),
        ),
    ],
)