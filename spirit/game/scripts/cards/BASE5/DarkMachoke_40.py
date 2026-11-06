from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import drag_off, opponent_has_benched
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="48715416-8bc6-5c5b-8876-97dd9efa674d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMachoke.Name",
    display_name="Dark Machoke",
    searchable_by=["Dark Machoke", "Stage 1", "DarkMachoke"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Before doing damage, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon. Do the damage to the new Defending Pok\u00e9mon. This attack can't be used if your opponent has no Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=drag_off,
            condition=opponent_has_benched,
        ),
        Attack(
            title="Knock Back",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)
