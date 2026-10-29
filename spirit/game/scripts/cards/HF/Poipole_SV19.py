from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm6 import knockout_reviver

card = PokemonCardDef(
    guid="e23cbb36-c683-59bc-afcd-7f375253697d",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    display_name="Poipole",
    searchable_by=["Poipole", "Basic", "Ultra Beast", "Poipole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=88,
    set_code="HF",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=803,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Knockout Reviver",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is Knocked Out, your opponent can't take any Prize cards for it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=knockout_reviver,
        ),
    ],
)
