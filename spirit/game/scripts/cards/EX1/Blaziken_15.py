from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    condition_attack, self_energy_discard_attack,
)


card = PokemonCardDef(
    guid="08ff0bb1-4eef-5376-89b7-c8640a2f23ab",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard a Fire Energy card attached to Blaziken.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)
