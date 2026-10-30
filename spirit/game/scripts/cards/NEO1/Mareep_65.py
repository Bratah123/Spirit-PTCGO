from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import static_electricity


card = PokemonCardDef(
    guid="008785c7-bd90-56c8-9e6e-4101c201e9a8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep",
    searchable_by=["Mareep", "Basic", "Mareep"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=179,
    abilities=[
        Attack(
            title="Static Electricity",
            game_text="For each Mareep in play, you may search your deck for a Lightning Energy card and attach it to Mareep. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=static_electricity,
        ),
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
