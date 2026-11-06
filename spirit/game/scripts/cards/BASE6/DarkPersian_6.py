from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import fascinate, opponent_has_benched


card = PokemonCardDef(
    guid="8771c112-a6bb-513e-b95f-02ea4ad1b09a",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkPersian.Name",
    display_name="Dark Persian",
    searchable_by=["Dark Persian", "Stage 1", "DarkPersian"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Fascinate",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fascinate,
            condition=opponent_has_benched,
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
