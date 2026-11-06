from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import dark_gaze_passive


card = PokemonCardDef(
    guid="eb52189a-0283-5bda-af5c-a9a6f4cded7e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Dark Gaze",
            game_text="As long as Umbreon is your Active Pok\u00e9mon, Benched Pok\u00e9mon (yours and your opponent's) can't use Pok\u00e9-Powers.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dark_gaze_passive,
        ),
        Attack(
            title="Sharp Claws",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)
