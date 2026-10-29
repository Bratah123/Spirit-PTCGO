from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dm import (
    dragon_wisdom,
)

card = PokemonCardDef(
    guid="bc682941-5896-5c07-a4ec-2f6e5772e2c4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=780,
    abilities=[
        Attack(
            title="Dragon Wisdom",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Dragon Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=dragon_wisdom,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)