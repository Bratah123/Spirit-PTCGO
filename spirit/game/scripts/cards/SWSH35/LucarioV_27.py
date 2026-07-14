from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="b409c006-964b-50e3-b0f6-7f0f5b4e4245",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    display_name="Lucario V",
    searchable_by=["Lucario V", "Basic", "V", "LucarioV"],
    subtypes=["Basic", "V"],
    collector_number=27,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Attack(
            title="Aura Sphere",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=snipe_attack(20, pool="bench", count=1, also_base=True),
        ),
        Attack(
            title="Beatdown Smash",
            game_text="During your next turn, this Pok\u00e9mon can't use Beatdown Smash.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            locks_next_turn=True,
        ),
    ],
)