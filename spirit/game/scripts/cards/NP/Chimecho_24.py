from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.ex import healing_sound


card = PokemonCardDef(
    guid="330f9202-4cdc-566a-ac60-faf255fa6328",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Resonate",
            game_text="Your opponent switches each Defending Pok\u00e9mon with his or her Benched Pok\u00e9mon. If your opponent has only 1 Benched Pok\u00e9mon, you choose the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=opponent_switches,
        ),
        Attack(
            title="Healing Sound",
            game_text="Remove 3 damage counters from each of your Active Pok\u00e9mon. Each Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=healing_sound(30),
        ),
    ],
)
